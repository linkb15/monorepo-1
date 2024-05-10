import {
  CalendarPlusIcon,
  FilePlusIcon,
  SignUpIcon,
  XmarkIcon,
} from '@monorepo/expo/shared/icons';
import { Colors, Spacings } from '@monorepo/expo/shared/static';
import { Pressable, StyleSheet } from 'react-native';
import MainModal from './MainModal';

const ACTIONS = [
  {
    title: 'Sign Up Process',
    Icon: SignUpIcon,
    route: '#',
  },
  {
    title: 'Add interaction',
    Icon: FilePlusIcon,
    route: '#',
  },
  {
    title: 'Add event',
    Icon: CalendarPlusIcon,
    route: '#',
  },
  {
    title: 'Add task',
    Icon: CalendarPlusIcon,
    route: '#',
  },
];

interface IMainPlusModalProps {
  closeModal: () => void;
  isModalVisible: boolean;
}

export default function MainPlusModal(props: IMainPlusModalProps) {
  const { isModalVisible, closeModal } = props;
  return (
    <MainModal
      actions={ACTIONS}
      isModalVisible={isModalVisible}
      closeModal={closeModal}
      bottomSection={
        <Pressable
          onPress={closeModal}
          accessibilityRole="button"
          accessibilityHint="Closing homepage main modal"
          style={styles.middleButton}
        >
          <XmarkIcon color={Colors.WHITE} />
        </Pressable>
      }
    />
  );
}

const styles = StyleSheet.create({
  middleButton: {
    marginTop: Spacings.sm,
    height: 66,
    width: 66,
    borderRadius: 100,
    backgroundColor: Colors.PRIMARY,
    alignItems: 'center',
    justifyContent: 'center',
    marginLeft: 'auto',
    marginRight: 'auto',
  },
});